<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>Batch Job Submission for Abaqus</h1>

  <p>This project provides a Python-based solution for submitting Abaqus jobs for all <code>.inp</code> files in the current directory. The script automates the process by creating and running batch files for each job.</p>

  <h2>Features</h2>
  <ul>
    <li><strong>Automated Job Submission:</strong> Submits Abaqus jobs for all <code>.inp</code> files in the current directory.</li>
    <li><strong>User Input for CPUs:</strong> Prompts the user to specify the number of CPUs for each job.</li>
    <li><strong>Batch File Creation:</strong> Creates a <code>.bat</code> file for each <code>.inp</code> file.</li>
    <li><strong>Command Execution:</strong> Runs the Abaqus command using the specified number of CPUs.</li>
  </ul>

  <h2>Usage Instructions</h2>
  <ol>
    <li>Place your <code>.inp</code> files in the directory where the script is located.</li>
    <li>Run the script using:
      <pre><code>python submit_jobs.py</code></pre>
    </li>
    <li>When prompted, enter the number of CPUs to use for each job (between 1 and 4).</li>
    <li>The script will create and run a <code>.bat</code> file for each <code>.inp</code> file.</li>
  </ol>

  <h2>Requirements</h2>
  <p>The following Python packages are required:</p>
  <ul>
    <li>os</li>
    <li>subprocess</li>
  </ul>
  <p>These libraries are part of the Python Standard Library, so no additional installation is required.</p>

  <h2>License</h2>
  <p>This project is licensed under the <strong>MIT License</strong>.</p>
  <p>You are free to use, modify, and distribute this software under the terms of the MIT License. If you use this software in your work, please provide appropriate credit to the developer.</p>

  <h2>Developer Information</h2>
  <ul>
    <li><strong>Developer:</strong> Your Name</li>
    <li><strong>Contact:</strong> <a href="https://wa.me/+923440907874">WhatsApp</a></li>
    <li><strong>Note:</strong> This tool is open-source. Feel free to modify it and share improvements.</li>
  </ul>
</body>
</html>
