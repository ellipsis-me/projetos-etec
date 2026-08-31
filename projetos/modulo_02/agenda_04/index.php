<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Funções e Repetidores</title>
</head>

<body>
    <?php
    $tarefas = array(
        "Estudar",
        "Trabalhar",
        "Treinar",
        "Dormir"
    );

    function listaTarefas($tarefas)
    {
        foreach ($tarefas as $tarefa) {
            echo "$tarefa <br/>";
        }
    }

    listaTarefas($tarefas)
    ?>
</body>

</html>