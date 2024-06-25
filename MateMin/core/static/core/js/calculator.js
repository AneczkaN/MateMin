// core/static/core/js/calculator.js

function handleButtonClick(button) {
    const expressionField = document.getElementById('id_expression');
    const currentValue = expressionField.value;
    const buttonValue = button.getAttribute('data-value');

    if (currentValue === 'Błąd') {
        expressionField.value = '';
    }

    if (currentValue === '0') {
        expressionField.value = buttonValue;
    } else {
        expressionField.value = currentValue + buttonValue;
    }
}

function evaluateExpression() {
    const expressionField = document.getElementById('id_expression');
    const currentValue = expressionField.value;

    try {
        let expression = currentValue.replace(/\^/g, '**');

        expression = expression.replace(/sqrt/g, 'Math.sqrt');
        expression = expression.replace(/sin/g, 'Math.sin');
        expression = expression.replace(/cos/g, 'Math.cos');
        expression = expression.replace(/tan/g, 'Math.tan');
        expression = expression.replace(/pi/g, 'Math.PI');
        expression = expression.replace(/e/g, 'Math.E');

        const result = eval(expression);
        expressionField.value = result.toString();
    } catch (error) {
        expressionField.value = 'Błąd';
    }
}

document.getElementById('calculator-form').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        evaluateExpression();
    }
});

document.getElementById('clear-button').addEventListener('click', function() {
    document.getElementById('id_expression').value = '';
});

document.querySelectorAll('.calc-button').forEach(button => {
    button.addEventListener('click', function() {
        handleButtonClick(button);
    });
});

document.getElementById('equal-button').addEventListener('click', function() {
    evaluateExpression();
});