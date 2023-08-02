function generate() {

    // get options
    const lang = document.getElementById("lang").value;
    let lb = parseInt(document.getElementById("lb").value);
    let ub = parseInt(document.getElementById("ub").value);

    if (!lb) {
        lb = 0;
    }
    if (!ub) {
        ub = lb + 1;
    }

    // generate string to insert
    let code;
    switch (lang) {

        case "Python":
            code = "def is_even(n: int) -> bool:";
            for (let i = lb; i <= ub; i++) {
                code += `\n    if n == ${i}:`;
                code += `\n        return ${i % 2 == 0 ? 'True' : 'False'}`;
            }
            code += "\n    raise Exception(f\"Number {n} unrecognized\")"
            break;

        case "Java":
            code = "// in UnrecognizedNumberException.java:\n" +
                   "public class UnrecognizedNumberException extends Exception { \n" + 
                   "    public UnrecognizedNumberException(String message) { \n" + 
                   "        super(message); \n" + 
                   "    }\n" + 
                   "}\n\n" + 
                   "// in OtherClassFile.java:\n" +
                   "public static boolean isEven(int numberToBeChecked) throws UnrecognizedNumberException {";
            for (let i = lb; i <= ub; i++) {
                code += `\n    if (numberToBeChecked == ${i}) {`;
                code += `\n        return ${String(i % 2 == 0)};`
                code += `\n    }`; 
            }
            code += "\n    throw new UnrecognizedNumberException(\"Input number not recognized in isEven function\");"
            code += "\n}";
            break;

        case "JavaScript":
            code = "function isEven(n) {"
            for (let i = lb; i <= ub; i++) {
                code += `\n    if (n === ${i}) {`;
                code += `\n        return ${String(i % 2 == 0)};`
                code += `\n    }`; 
            }
            code += "\n    throw new Error(`Number ${n} unrecognized`);"
            code += "\n}";
            break;
        case "Bash":
            function getNumbers(lb, ub, even) {
                let output = 'echo "';
                let filename = `tmp_${even ? 'even' : 'odd'}.txt`;
                for (let i = lb; i <= ub; i++) {
                    if ((even && i % 2 == 0) || (!even && i % 2 == 1)) {
                        output += "z" + String(i) + " ";
                    }
                    if ((i - lb) % 20 === 19) {
                        output += `" >> ${filename}\necho "`;
                    }
                }
                output += `" >> ${filename}\n`;
                return output;
            }
            code = "#!/bin/bash\n" + 
                   `${getNumbers(lb, ub, true)}\n` + 
                   `${getNumbers(lb, ub, false)}\n` +
                   'if [ cat tmp_even.txt | grep "z$1 "]; then\n' + 
                   "    echo True\n" +
                   "fi\n" +
                   'if [ cat tmp_odds.txt | grep "z$1 "]; then\n' +
                   "    echo False\n" +
                   "fi\n" +
                   "rm tmp_even.txt tmp_odd.txt";
            break;
        case "SQL":
            code =  "CREATE FUNCTION IF NOT EXISTS is_even(number_to_check INT) RETURNS VARCHAR(1) AS \n" + 
                    "$$\n" + "DECLARE\n" + "    output VARCHAR(1);\n" + 
                    "    query TEXT := 'SELECT is_even FROM numbers WHERE n = number_to_check'\n" + "BEGIN\n" + 
                    "    CREATE TABLE numbers (\n        n INT UNIQUE,\n        is_even VARCHAR(1) NOT NULL\n    );\n\n";
            for (let i = lb; i <= ub; i++) {
                code += `    INSERT INTO numbers (n, is_even) VALUES (${i}, ${i % 2 === 0 ? "'y'" : "'n'"});\n`;
            }
            code += "\n    EXECUTE query INTO output;\n" + "    RETURN output;\n" + "END\n" + "$$";
        // TODO LANGS: shell, C, C++, C# ?, SQL? lol, others
    }

    // show output
    document.getElementById("code").removeAttribute("hidden");
    document.getElementById("code").innerHTML = `<pre><code class="language-${lang.toLowerCase()}">${code}</code></pre>`;

    // highlught syntax
    hljs.highlightAll();
}