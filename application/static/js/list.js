$('#table').DataTable({
    "paging": false,
    "scrollY": "650px",
    "pageLength": 99999,
    columnDefs: [
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
});
