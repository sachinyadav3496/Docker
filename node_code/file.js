const fs = require('fs');
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

readline.question("Enter filename: ", filename => {
    readline.question("Enter Some Text: ", text => {
        fs.writeFile(`${filename}.txt`, text, err => {
            if (err) throw err
            console.log("File has been created.!");
            readline.close();
        });
    });
});