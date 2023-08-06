# Seams SDK

## Setting up Python SDK environment
1. To set up the Python SDK environment you must first install Anaconda here: https://www.anaconda.com/products/distribution 
2. Add the correct environment variables to VS Code
    - Search for Advanced system settings
    - Environment variables
    - Under system variables -> path add the below 3 things to allow you to run "conda" commands in VS Code:
        - C:\ProgramData\Anaconda3
        - C:\ProgramData\Anaconda3\Library\bin
        - C:\ProgramData\Anaconda3\Scripts
3. Navigate to the root directory of the SDK project after cloning and run
```bash
conda env create -f sdk_env.yaml
```
4. Once the above command is completed run
```bash
conda activate sdk
```
