# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import base64

INPUT_FILE = 'image.jpg'
OUTPUT_FILE = '/tmp/image_b64.json'

"""Open image and convert it to Base64"""
with open(INPUT_FILE, 'rb') as input_file:
  jpeg_bytes = base64.b64encode(input_file.read()).decode('utf-8')
  predict_request = '{"image_bytes": {"b64": "%s"}}' % jpeg_bytes
  # Write JSON to file
  with open(OUTPUT_FILE, 'w') as output_file:
    output_file.write(predict_request)
