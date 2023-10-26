{
  description = "Article";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let pkgs = import nixpkgs { system = "aarch64-darwin"; };
    in {
      devShell.aarch64-darwin = pkgs.mkShell {
        buildInputs = [
          pkgs.python3
          pkgs.python3Packages.pip
          pkgs.python3Packages.pandas
          pkgs.python3Packages.matplotlib
          pkgs.python3Packages.seaborn
        ];
      };
    };
}
