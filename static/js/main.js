document.addEventListener("DOMContentLoaded", () => {
  const telefoneInput = document.querySelector("#ctelefone");
  const cepInput = document.querySelector("#ccep");

  const mascaraTel = {
    mask: [{ mask: "(00) 0000-0000" }, { mask: "(00) 00000-0000" }],
  };
  IMask(telefoneInput, mascaraTel);

  const mascaraCep = {
    mask: "00000-000",
  };
  IMask(cepInput, mascaraCep);
  const teste = IMask(cepInput, mascaraCep);
  teste.on("complete", async () => {
    const cepDigitado = cepInput.value;
    try {
      const resposta = await fetch("/buscar_cep", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ cep: cepDigitado }),
      });
      const dados = await resposta.json();

      if (resposta.ok) {
        document.querySelector("#cbairro").value = dados.bairro;
        document.querySelector("#cbairro").readOnly = true;
        document.querySelector("#crua").value = dados.logradouro;
        document.querySelector("#crua").readOnly = true;
      } else {
        alert(dados.erro);
      }
    } catch (erro) {
      console.error("Erro na requisição do CEP:", erro);
    }
  });
});
