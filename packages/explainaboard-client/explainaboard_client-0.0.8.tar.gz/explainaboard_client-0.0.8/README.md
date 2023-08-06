# ExplainaBoard Client

This is a command line and API client that makes it easy for you to evaluate systems
using [ExplainaBoard](https://explainaboard.inspiredco.ai).

## Preparation

### Install

- For CLI/api users
    - `pip install explainaboard_client`
- For explainaboard client developers
    - `pip install ".[dev]"`

### Acquiring a Login and API Key

First, create an account at the [ExplainaBoard](https://explainaboard.inspiredco.ai)
site and remember the email address you used. Once you are logged in, you can click on
the upper-right corner of the screen, and it will display your API key, which you can
copy-paste.

You can save these into environmental variables for convenient use in the commands
below:

```
export EB_EMAIL="[your email]"
export EB_API_KEY="[your API key]"
```

## Usage

### Evaluating/Browsing/Deleting Systems from the Command Line

**Evaluating Systems:** The most common usage of this client will probably be to
evaluate systems on the ExplainaBoard server. You can do that from the
command line.

If you are using a pre-existing dataset viewable from the
[ExplainaBoard datasets](https://explainaboard.inspiredco.ai/datasets)
page then you can use something like the following command:

```
python -m explainaboard_client.cli.evaluate_system \
  --email $EB_EMAIL --api_key $EB_API_KEY \
  --task [TASK_ID] \
  --system_name [MODEL_NAME] \
  --system_output [SYSTEM_OUTPUT] --output_file_type [FILE_TYPE] \
  --dataset [DATASET] --sub_dataset [SUB_DATASET] --split [SPLIT] \
  --source_language [SOURCE] --target_language [TARGET] \
  [--public]
```

You will need to fill in all the settings appropriately, for example:
* `[TASK_ID]` is the ID of the task you want to perform. A full list is [here](https://github.com/neulab/explainaboard_web/blob/main/backend/src/impl/tasks.py).
* `[MODEL_NAME]` is whatever name you want to give to your model.
* `[SYSTEM_OUTPUT]` is the file that you want to evaluate.
* `[FILE_TYPE]` is the type of the file, "text", "tsv", "csv", "conll", or "json".
* `[DATASET]`, `[SUB_DATASET]` and `[SPLIT]` indicate which dataset you're evaluating
  a system output for.
* `[SOURCE]` and `[TARGET]` language indicate the language code of the input and output of
  the system. Please refer to the [ISO-639-3](https://iso639-3.sil.org/code_tables/639/data) list for the 3-character 693-3 language codes. Enter `other-[your custom languages]` if the dataset uses custom languages. Enter `none` if the dataset uses other modalities like images. If the inputs and outputs are the in the same language you only need to
  specify one or the other.
* By default your systems will be private, but if you add the `--public` flag they
  will be made public on the public leaderboards and system listing.

**Evaluating w/ Custom Datasets:** You can also evaluate results for custom datasets
that are not supported by DataLab yet:

```
python -m explainaboard_client.cli.evaluate_system \
  --email $EB_EMAIL --api_key $EB_API_KEY \
  --task [TASK_ID] \
  --system_name [MODEL_NAME] \
  --system_output [SYSTEM_OUTPUT] --output_file_type [FILE_TYPE] \
  --custom_dataset [CUSTOM_DATASET] --custom_dataset_file_type [FILE_TYPE] \
  --source_language [SOURCE] --target_language [TARGET]
```

with similar file and file-type arguments to the system output above. If you're
interested in getting your datasets directly supported within ExplainaBoard, please
open an issue or send a PR to [DataLab](https://github.com/expressai/datalab), and we'll
be happy to help out!

**Finding Uploaded Systems:** You can also find systems that have already been evaluated
using the following syntax
```
python -m explainaboard_client.cli.find_systems \
  --email $EB_EMAIL --api_key $EB_API_KEY --output_format tsv
```
By default this outputs in a summarized TSV format (similar to the online system
browser), but you can set `--output_format json` to get more extensive information.
There are many options for how you can specify which systems you want to find, which you
can take a look at by running `python -m explainaboard_client.cli.find_systems` without
any arguments.

**Deleting System Outputs:** You can delet existing system outputs using the following
command:
```
python -m explainaboard_client.cli.delete_systems \
  --email $EB_EMAIL --api_key $EB_API_KEY --system_ids XXX YYY
```
Here the `system_ids` are the unique identifier of each system returned in the
`system_id` field of the JSON returned by the `find_systems` command above. The system
IDs are *not* the system name as displayed in the interface.

### Evaluating Systems on Benchmarks from the Command Line
Instead of simply evaluating an individual system, another common scenario is 
to submit a group of systems to a benchmark (e.g., GLUE). To achieve this goal,
you can follow the command below: 

```shell
python -m explainaboard_client.cli.evaluate_benchmark \
      --email XXX  \
      --api_key YYY \
      --system_name your_system \
      --system_outputs submissions/* \
      --benchmark benchmark_config.json \
      --server local
```
where
* `--email`: the email of your explainaboard account
* `--api_key`: your API key
* `--system_name`: the system name of your submission. Note: this assumes that all
system output share one system name.
* `--benchmark`: the benchmark config file (you can check out this [doc](TBC) to see how to configure the benchmark.)
* `system_outputs`: system output files. Note that the order of `system_outputs` files should
strictly correspond to the dataset order of `datasets` in `benchmark_config.json`.
* By default, your systems will be private, but if you add the `--public` flag, they
  will be made public on the public leaderboards and system listing.
  
Here is one [example](./example/benchmark/gaokao/) for the `Gaokao` benchmark.



### Programmatic Usage

Please see examples in `./tests`.
We will be working on more examples and documentation shortly.




## Update

There are two packages associated with this CLI: `explainaboard_api_client` and `explainaboard_client`
- `explainaboard_api_client`: auto generated according to OpenAPI definition specified in [openapi.yaml](https://github.com/neulab/explainaboard_web/tree/main/openapi). Version of this client is specified in the same yaml file (`info.version`).
  - To update: `pip install -U explainaboard_api_client` or specify a specific version
  - To check the API version used in the live environment: `curl https://explainaboard.inspiredco.ai/api/info` (this information will be added to the UI in the future)
- `explainaboard_client`: a thin wrapper for the API client to make it easy to use. It helps users configure API keys, choose host names, load files from local FS, etc. Usually, this package is relatively stable so you don't need to update unless a new feature of the CLI is released.
  - To update: `pip install -U explainaboard_client`



