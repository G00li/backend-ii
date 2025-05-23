# Aula 16 – CI/CD com GitHub Actions

Exemplo de workflow de CI para rodar testes em múltiplas versões do Python.

## Como funciona

- O workflow é disparado em push ou pull request.
- Testa o projeto nas versões 3.8, 3.9, 3.10 e 3.11 do Python.
- Instala as dependências do requirements.txt se existir.
- Roda todos os testes com pytest.

## Como usar

1. Coloque o arquivo `ci.yml` em `.github/workflows/` do seu projeto.
2. Faça um push para o GitHub.
3. Veja o resultado na aba "Actions" do seu repositório. 