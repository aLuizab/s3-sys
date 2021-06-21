## AWS S3 Bucket Analysis

### Local configuration

First of all, you need to configure your local environment to run the script. 

Configure your AWS credentials using [this](https://docs.aws.amazon.com/cli/latest/reference/configure/#examples) documentation.

### Instalation

```
git clone https://github.com/aLuizab/s3-sys.git
cd s3-sys
pip3 install -r requirements.txt
python3 -s3-sys.py
```
### Output

```
Name: bucket-ze | Creation Date: 2021-06-13 15:13:34+00:00 | Objects: 3 | Size: 1.34 MB | Last Modified: 2021-06-13 22:01:29+00:00
--------------------------
Name: bucket-zed | Creation Date: 2021-06-13 21:58:29+00:00 | Objects: 1 | Size: 585.64 KB | Last Modified: 2021-06-13 22:01:29+00:00
--------------------------
Name: teste-bucket111 | Creation Date: 2021-06-15 05:47:57+00:00 | Objects: 0 | Size: 0B | Last Modified: 2021-06-13 22:01:29+00:00
```