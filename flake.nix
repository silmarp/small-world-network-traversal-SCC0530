{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/master";
    flake-utils.url = "github:numtide/flake-utils";
    # TODO Change to using dream2nix, mach-nix is now unmantained
    mach-nix.url = "mach-nix/3.5.0";
  };

  outputs = {self, nixpkgs, flake-utils, mach-nix }@inp:
  flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        pythonEnv = mach-nix.lib.${system}.mkPython {
          python = "python310";
          requirements = builtins.readFile ./src/requirements.txt;
        };
        devPkgs = with pkgs; [
          nodePackages.pyright
        ];
      in
      {
        devShell = pkgs.mkShell {
          nativeBuildInputs = [
            pythonEnv
            devPkgs
          ];
        };
      });
}
