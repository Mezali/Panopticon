$('#table').DataTable({
    "paging": false,
    "scrollY": "705px",
    "pageLength": 99999,
    columnDefs: [
        {
            "targets": "no-sort", // Aplicar a configuração apenas às colunas com a classe "no-sort"
            "orderable": false,   // Não permitir classificação
            "searchable": false   // Não permitir pesquisa
        },
        {"width": "100px", "targets": 0},
        {"width": "50px", "targets": 2},
        {orderable: false, targets: [2]},
        {
            targets: -1,
            className: 'dt-body-right'
        }
    ],
    "language": {
        "sProcessing": "Processando...",
        "sLengthMenu": "",
        "sZeroRecords": "Nenhum registro encontrado",
        "sEmptyTable": "Nenhum dado disponível nesta tabela",
        "sInfo": "Mostrando _END_ registros",
        "sInfoEmpty": "Mostrando 0 registros",
        "sInfoFiltered": "(filtrado de um total de _MAX_ registros)",
        "sInfoPostFix": "",
        "sSearch": "Buscar:",
        "sUrl": "",
        "sInfoThousands": ",",
        "sLoadingRecords": "Carregando...",
        "oPaginate": {
            "sFirst": "",
            "sLast": "",
            "sNext": "",
            "sPrevious": ""
        },
        "oAria": {
            "sSortAscending": ": Ativar para ordenar a coluna de forma ascendente",
            "sSortDescending": ": Ativar para ordenar a coluna de forma descendente"
        }
    }
})

$("#form").submit(function (event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    // Obtém todos os valores dos campos "colaborador_estado"
    var colaborador = $('.usuarios').map(function () {
        return $(this).val();
    }).get();

    // Envia os dados para o Flask usando Ajax
    $.ajax({
        url: "/sua-rota-flask-aqui", // Substitua pela rota correta do Flask
        type: "POST",
        data: {
            colaborador: colaborador
        },
        success: function (response) {
            // Lidar com a resposta do Flask, se necessário
            console.log(response);
        },
        error: function (error) {
            console.error(error);
        }
    });
});
