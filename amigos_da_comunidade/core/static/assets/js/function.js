/**
  Função faz a busca do cep e retorna um JSON
**/

$(function(){
  loadState = function(value, city){
    var url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados";
    var opcoes = "<option value=''>Escolha UF</option>";
    $.getJSON( url, function(states){
      states = states.sort(function(a, b) {
        var x = a['nome']; var y = b['nome'];
        return ((x < y) ? -1 : ((x > y) ? 1 : 0));
      });
      $.each(states, function(i, state){
          selected = "";
          if (state.sigla==value){
            selected = "selected";
            loadCity(state.id, city);
          }
          opcoes += '<option '+selected+' value="'+state.sigla+'" id="'+state.id+'">'+state.nome+'</option>';
      });
      $("#id_state").html(opcoes);

    });
  }
  loadCity = function (UFid, cidade){
    var url = "http://servicodados.ibge.gov.br/api/v1/localidades/estados/"+UFid+"/municipios";
    $("#id_city").empty();
    var opcoes = "";
    $.getJSON( url, function(cities){
      cities = cities.sort(function(a, b) {
        var x = a['nome']; var y = b['nome'];
        return ((x < y) ? -1 : ((x > y) ? 1 : 0));
      });
      $.each(cities, function(i, city){
          selected = "";
          if (city.nome==cidade){
            selected = "selected";
          }
          opcoes += '<option '+selected+' value="'+city.nome+'">'+city.nome+'</option>';
      });
      $("#id_city").html(opcoes);
    });
  }

});
