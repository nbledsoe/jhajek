import boto3

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html

s3 = boto3.client('s3')
# s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
s3.download_file('jrh-544-raw-bucket', '20160812_205519.jpg', 'current-image.jpg')

