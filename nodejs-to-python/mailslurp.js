let {PythonShell} = require('python-shell')

async function main() {
	const MailSlurp = require('mailslurp-client').default;

	const apiKey = 'api-key';
	const mailslurp = new MailSlurp({ apiKey });
	const { id, emailAddress } = await mailslurp.createInbox();

	console.log(id);
	console.log(emailAddress);

	var options = {
	    mode: 'text',
	    args: [emailAddress]
	};

	PythonShell.run('sample.py', options, function (err, results) {
	    if (err) throw err;
	    // results is an array consisting of messages collected during execution
	    console.log('results: %j', results);
	});

}

main();