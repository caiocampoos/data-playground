# Getting Started with PySpark

This tutorial demonstrates how to set up PySpark and a data lake running in Docker in the easiest way possible on Ubuntu using WSL.

Before you begin, ensure you have one of the latest versions of PYTHON and PIP installed on your Ubuntu system.


### 1. Install the Java SDK:

PySpark requires the Java Development Kit (JDK) to function. You can install it with the following command:

```
sudo apt install default-jdk
```

### 2. Install PySpark:

Now that the JDK is installed, you can install PySpark using PIP:

```
pip install pyspark
```

### 3. Install Docker:
Docker is required to run PySpark in a container. Follow these steps to install Docker:

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce
```
### 4. Execute Pyspark 

You can verify if the installation was successful by running PySpark:

```
pyspark
```

### 5. Runing Pyspark into a docker
Once the installation is successful, you can easily run PySpark within a Docker container:

```
docker run -it --rm spark:python3 /opt/spark/bin/pyspark
```

Try executing this [sample](./index.py) code!