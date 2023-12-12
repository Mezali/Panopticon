$('#adicionar').click(function (event) {
    event.preventDefault();
    processarPlanilha('adicionar', '/massa-add');
});


$('#excluir').click(function (event) {
    event.preventDefault();
    excluirColaboradores()
});

function processarPlanilha(action, url) {
    let inputFile = document.getElementById('planilha');
    let file = inputFile.files[0];

    let reader = new FileReader();
    reader.onload = function (e) {
        let dadosPlanilha = e.target.result;
        $('#dadosPlanilha').val(dadosPlanilha);

        let formData = new FormData();
        formData.append('acao', action);
        formData.append('file', file);

        Swal.fire({
            title: 'Carregando...', allowEscapeKey: false, allowOutsideClick: false, didOpen: () => {
                Swal.showLoading();
            }
        });

        $.ajax({
            type: 'POST',
            url: url,
            data: formData,
            contentType: false,
            processData: false,
            success: function (response) {
                console.log('Resposta do Flask:', response);

                if (response.status === 200) {
                    Swal.fire({
                        title: 'Operação concluída',
                        text: response.mensagem,
                        icon: 'success',
                        confirmButtonText: 'Fechar'
                    }).then(() => {
                        location.reload();
                    });
                } else {
                    exibirErro(response.error);
                }
            },
            error: function (xhr) {
                exibirErro('Ocorreu um erro ao processar os dados: ' + xhr.responseJSON.error);
            }
        });
    };

    function exibirErro(mensagem) {
        Swal.fire({
            title: 'Erro', text: mensagem, icon: 'error', confirmButtonText: 'Fechar'
        });
    }
}

function excluirColaboradores() {
    Swal.fire({
        title: 'Carregando...', allowEscapeKey: false, allowOutsideClick: false, didOpen: () => {
            Swal.showLoading();
        }
    });

    $.ajax({
        type: 'POST',
        url: '/del-geral',
        contentType: false,
        processData: false,
        success: function (response) {
            console.log('Resposta do Flask:', response);

            if (response.status === 200) {
                Swal.fire({
                    title: 'Operação concluída',
                    text: response.mensagem,
                    icon: 'success',
                    confirmButtonText: 'Fechar'
                }).then(() => {
                    location.reload();
                });
            } else {
                alert(response.error);
            }
        },
    });
}