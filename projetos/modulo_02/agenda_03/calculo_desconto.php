<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST["txtNome"];
    $valorCompra = $_POST["txtValorCompra"];
    $formaPagamento = $_POST["cmbPag"];
    $desconto = 0;

    // ERRO: cálculo incorreto para boleto e depósito
    if ($formaPagamento == "cartaoCredito") {
        $desconto = 0;
        $mensagem = "Olá $nome, sua compra de R$ ".number_format($valorCompra, 2, ',', '.')." foi realizada com cartão de crédito. Não há desconto.";
    } elseif ($formaPagamento == "boleto") {
        // $desconto = $valorCompra * 0.1; // ERRO: deveria ser 8% para boleto
        $desconto = $valorCompra * 0.08;
        $valorComDesconto = $valorCompra - $desconto;
        $mensagem = "Olá $nome, sua compra de R$ ".number_format($valorCompra, 2, ',', '.')." foi realizada com boleto. Seu desconto é de R$ ".number_format($desconto, 2, ',', '.').".<br> Valor total com desconto: R$ ".number_format($valorComDesconto, 2, ',', '.')."";
    } elseif ($formaPagamento == "deposito") {
        $desconto = $valorCompra * 0.1;
        $valorComDesconto = $valorCompra - $desconto;
        $mensagem = "Olá $nome, sua compra de R$ ".number_format($valorCompra, 2, ',', '.')." foi realizada com depósito. Seu desconto é de R$ ".number_format($desconto, 2, ',', '.').".<br> Valor total com desconto: R$ ".number_format($valorComDesconto, 2, ',', '.')."";
    } else {
        $mensagem = "Forma de pagamento inválida.";
    }

    // ERRO: mensagem final não mostra valor com desconto
    echo "<div class='w3-panel w3-green'>$mensagem</div>";
}
?>