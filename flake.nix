{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/master";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {self, nixpkgs, flake-utils, }@inp:
  flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        devPkgs = with pkgs; [
          nodePackages.pyright
        ];
      in
      {
        devShell = pkgs.mkShell {
          nativeBuildInputs = [
            pkgs.python310
            pkgs.python310Packages.pip
            pkgs.python310Packages.virtualenv
            devPkgs
          ];
          /*
          shellHook = ''
            source ./VENV/bin/activate
          '';
          */
        };
      });
}
