/**
  Função faz a busca do cep e retorna um JSON
  **/

  $(document).ready(function(){
    function limpa_formulario_cep() {
      // Limpa valores do formulário de cep.
      $("#id_country").val("");
      $("#id_state").val("");
      $("#id_city").val("");
      $("#id_neighborhood").val("");
      $("#id_street").val("");
      $("#id_complement").val("");
      $("#id_zip_code").val("");
    }

    function inputCepVemelho(){
      $('#id_zip_code').addClass('input-vermelho');
      $('#lb_zip_code').text("CEP Inválido");
      $('#lb_zip_code').addClass('text-danger');
    }

    function removeClassInput(){
      $('#id_zip_code').removeClass('input-vermelho');
      $('#lb_zip_code').removeClass('text-danger');
      $('#lb_zip_code').text("CEP");
    }

    function formatoCepInvalido(){
      $('#id_zip_code').addClass('input-vermelho');
      $('#lb_zip_code').text("Formato de CEP inválido");
      $('#lb_zip_code').addClass('text-danger');
    }

  //Quando o campo cep perde o foco.
  $("#id_zip_code").blur(function() {

    //Nova variável "cep" somente com dígitos.
    var cep = $(this).val().replace(/\D/g, '');
    //Verifica se campo cep possui valor informado.
    if (cep != "") {
      //Expressão regular para validar o CEP.
      var validacep = /^[0-9]{8}$/;
      //Valida o formato do CEP.
      if(validacep.test(cep)) {
        //Preenche os campos com "..." enquanto consulta webservice.
        $("#id_country").val("...");
        $("#id_state").val("...");
        $("#id_city").val("...");
        $("#id_neighborhood").val("...");
        $("#id_street").val("...");
        $("#id_complement").val("...");

        //Consulta o webservice viacep.com.br/
        $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {
          if (!("erro" in dados)){
            //Atualiza os campos com os valores da consulta.
            $("#id_country").val('Brasil');
            $("#id_state").val(dados.uf);
            $("#id_city").val(dados.localidade);
            $("#id_neighborhood").val(dados.bairro);
            $("#id_street").val(dados.logradouro);
            $("#id_complement").val(dados.complemento);
            $("#id_number").focus();
            removeClassInput();
          }else {
            //CEP pesquisado não foi encontrado.
            limpa_formulario_cep();
            inputCepVemelho();
          }
        });
      }else {
        //cep é inválido.
        limpa_formulario_cep();
        formatoCepInvalido();
      }
    }else {
      //cep sem valor, limpa formulário.
      limpa_formulario_cep();
    }
  });
});
