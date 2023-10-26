{
  description = "Article";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }: {
    devShell.aarch64-darwin = (import nixpkgs { }).mkShell {
      buildInputs = [
        nixpkgs.python3
        nixpkgs.python3Packages.pip
        nixpkgs.python3Packages.pandas
        nixpkgs.python3Packages.matplotlib
        nixpkgs.python3Packages.seaborn
      ];
    };
  };
}
