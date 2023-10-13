$('#table').DataTable({
    "paging": false,
    "scrollY": "675px",
    "pageLength": 99999,
    columnDefs: [
        {"width": "20px", "targets": 0},
        {"width": "50px", "targets": 1},
        {"width": "50px", "targets": 3},
        {orderable: false, targets: [0, 3], "searchable": false},
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


$('#excluir').click(function (event) {
    event.preventDefault();

    Swal.fire({
        title: 'Tem certeza?',
        text: 'Esta ação irá excluir os colaboradores selecionados.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sim, excluir',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Exibir um Swal com uma tela de carregamento
            Swal.fire({
                title: 'Carregando',
                text: 'Aguarde enquanto a operação está em andamento...',
                allowOutsideClick: false,
                onBeforeOpen: () => {
                    Swal.showLoading();
                }
            });

            let colaboradores = [];

            $('.user-checkbox').each(function () {
                let id = $(this).attr('id');
                let checkBoxEstado = $(this).is(':checked');

                // Verifique se o checkbox está marcado (estado é true) antes de adicioná-lo à lista.
                if (checkBoxEstado) {
                    colaboradores.push({nome: id});
                }
            });
            console.log(colaboradores);

            // Fazer uma solicitação AJAX usando jQuery
            $.ajax({
                type: 'POST',
                url: '/del-colaborador',
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
                    }).then(() => {
                        // Recarregue a página após fechar o Swal
                        location.reload();
                    });

                    // Desmarque todos os checkboxes após a exclusão
                    $('.user-checkbox').prop('checked', false);
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
        }
    });
});

