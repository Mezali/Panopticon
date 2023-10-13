$('#table').DataTable({
    "paging": false,
    "scrollY": "675px",
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

$('#form').submit(function (event) {
    event.preventDefault();

    let colaboradores = [];

    $('.user-checkbox').each(function () {
        let id = $(this).attr('id');
        let checkBoxEstado = $(this).is(':checked');
        colaboradores.push({estado: checkBoxEstado, nome: id});
    });

    console.log(colaboradores);

    // Exibir um Swal com uma tela de carregamento
    Swal.fire({
        title: 'Carregando',
        text: 'Aguarde enquanto a operação está em andamento...',
        allowOutsideClick: false,
        onBeforeOpen: () => {
            Swal.showLoading();
        }
    });

    // Exibir um Swal com uma tela de carregamento
    Swal.fire({
        title: 'Carregando',
        text: 'Aguarde enquanto a operação está em andamento...',
        allowOutsideClick: false,
        showConfirmButton: false, // Esconde o botão de fechar
        onBeforeOpen: () => {
            Swal.showLoading();
        }
    });

    $.ajax({
        type: 'POST',
        url: '/kitedit',
        data: JSON.stringify(colaboradores),
        contentType: 'application/json',
        success: function (response) {
            // Feche o Swal após a conclusão da operação
            Swal.close();

            Swal.fire({
                title: 'Operação concluída',
                text: response.message,
                icon: 'success',
                confirmButtonText: 'Fechar'
            });
        },
        error: function (error) {
            // Feche o Swal em caso de erro
            Swal.close();

            Swal.fire({
                title: 'Erro',
                text: 'Ocorreu um erro ao processar os dados.',
                icon: 'error',
                confirmButtonText: 'Fechar'
            });
        }
    });


});