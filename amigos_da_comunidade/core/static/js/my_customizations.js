$(document).ready(function(){
	$("#id_birth_date").datepicker({
		format: "dd/mm/yyyy",
		todayBtn: "linked",
		language: "pt-BR",
		autoclose: true,
		todayHighlight: true
	});
	$('#id_phone').mask('(00) 0 0000-0000');
	$('#id_zip_code').mask('00000-000');
	$('#id_birth_date').mask('00/00/0000');
	$('#id_cpf').mask('000.000.000-00');

	// Dados da pessoa
	var username = $('#id_username');
	var name = $('#id_name');
	var email = $('#id_email');

	// minhas variaveis
	var person = $('#person');
    var address = $('#address1');
    var contact = $('#contact1');
	var active_tab_class = 'active';

	function removeAddClassAtiveBtnProximoDados(){
	    contact.removeClass(active_tab_class);
	    person.removeClass(active_tab_class);
	    address.addClass(active_tab_class);
	}
	function removeAddClassAtivebtnProximoEndereco(){
	    person.removeClass(active_tab_class);
	    address.removeClass(active_tab_class);
		contact.addClass(active_tab_class);
	}
	function removeAddClassAtivebtnAnteriorPaciente(){
	    person.addClass(active_tab_class);
	    address.removeClass(active_tab_class);
		contact.removeClass(active_tab_class);
	}
	function removeAddClassAtivebtnAnteriorEndereco(){
		contact.removeClass(active_tab_class);
	    person.removeClass(active_tab_class);
	    address.addClass(active_tab_class);
	}
	$('#btnProximoDados').click(function() {
		removeAddClassAtiveBtnProximoDados();
	});
	$('#btnAnteriorDados').click(function() {
		removeAddClassAtivebtnAnteriorPaciente();
	});
	$('#btnAnteriorEndereco').click(function() {
		removeAddClassAtivebtnAnteriorEndereco();
	});
	$('#btnProximoEndereco').click(function() {
		removeAddClassAtivebtnProximoEndereco();
	});

});
