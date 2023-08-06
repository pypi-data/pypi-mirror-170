# SPDLogger

SPDLogger package included python logger, sentry, ML metrics tracking system like Mlflow or Neptune.AI

#### User guide
1. To install SPDLogger,

```
# spda
pip install --extra-index-url https://pypiserver.qa.di.in.spdigital.sg:4443/simple/ spdlogger 

# spga
pip install --extra-index-url https://pypiserver-spga.qa.di.in.spdigital.sg/simple/ spdlogger
```

2. Import the module,
```
from spdlogger import SPDLogger
```

3. Use default settings,
```
logger = SPDLogger()
```

** Notes: Python logger settings are stored in stored in settings.toml on top of Dynaconf
          Users can change the settings by specify the other configfile or simply input the argument into the module class, for example:

```
** Note that configfile must include section of environment to indicate the section to load
** environment is specified in .env 

# for example:
conf.toml:
[development]
LOGGING_FILE = true
LOGGING_FILENAME = "logfile.log"
METRIC_SYSTEM = "MLFLOW"
SENTRY = true

logger = SPDLogger(config='/full/path/to/your/conf.toml')

** for others format, please refer to https://dynaconf.readthedocs.io/en/docs_223/guides/examples.html
```

```
# default logging level = "DEBUG"
logger = SPDLogger(LOGGING_LEVEL="INFO")   
```

4. To log into file,
```
logger = SPDLogger(LOGGING_FILE=True)
```

5. To log into Sentry,
```
logger = SPDLogger(SENTRY=True)
```

6. Users can log the message/errors according to severity: DEBUG, INFO, WARNING, ERROR, CRITICAL, FATAL, EXCEPTION by simply:
```
logger.debug("This is info message") 
....
logger.exception("This is debug message")
```

7. To log ML params and metrics,  need to turn on the ML tracking system by:
```
# default is "NA"
logger = SPDLogger(METRIC_SYSTEM="MLFLOW")  
OR
logger = SPDLogger(METRIC_SYSTEM="NEPTUNE.AI")
```

8. To log ML params, simply input key and value by:
logger.params(key, value)  
```
logger.params("learning_rate", 0.15)
```
OR key and value in dictionary form:
```
parameters = {
    "dense_units": 128,
    "activation": "relu",
    "dropout": 0.23,
    "batch_size": 64,
    "n_epochs": 30,
}

logger.params("parameters", parameters)
```

9. To log ML metrics, simply input key and value by:
logger.metrics(key, value)
```
logger.metrics("f1 score", 0.7)
```
OR log metrics in loop:
```
for epoch in range(parameters["n_epochs"]):
    loss = 0.5 ** epoch
    logger.metrics("train/epoch/loss",loss)
```

** Notes: for Neptune.AI, can organise the log outputs by specify folder/subfolder/

10. To log model into ML tracking system,
logger.model(model_name, model, model_type)
```
logger.model("linear_best_model", model, "sklearn") # specify model type to use mlflow supported log function
OR
logger.model("linear_best_model", model) # model is log as pickle file under artifacts
```

** Notes: for MLFLOW, refer to https://www.mlflow.org/docs/latest/models.html#model-api to view list of supported models

11. To log file into ML tracking system,
logger.file(file_name, file)
```
logger.file("1st_exp_log", "./logfile.log")
```

12. To register model:
logger.register_model(model_name, model, stage)
```
logger.register_model("linear_model", model, "staging")
```







