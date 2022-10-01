# Object Detection API

This is a simple Flask wrapper around the Yolo V5 object detection model. An image can be provided via a POST request and a JSON response is returned containing details of the detected objects.

## Usage

```bash
docker-compose run --service-ports yolo-server
```

The first time you run it, it will have to download the pre-trained yolov5 model which make take a while on slower connections.

The server will the be available locally on port 5001 and can be used as follows:

```bash
curl --request POST \
  --url http://127.0.0.1:5001/process_image \
  --header 'Content-Type: multipart/form-data' \
  --form 'image=@/Path/to/an/image'
```

And will return results in the form:

```json
[
	{
		"class": 0,
		"confidence": 0.8731165528297424,
		"name": "person",
		"xmax": 5179.173828125,
		"xmin": 3863.4697265625,
		"ymax": 3427.361572265625,
		"ymin": 0.0
	},
	{
		"class": 0,
		"confidence": 0.793181300163269,
		"name": "person",
		"xmax": 3772.135009765625,
		"xmin": 1624.6787109375,
		"ymax": 3430.2548828125,
		"ymin": 326.4531555175781
	}
]
```

## Development

It includes a `.devcontainer` definition for VSCode so as long as you have the vscode container extension installed, you should be able to use it as is. The decontainer setup will automatically run the server on port 5001 which should automatically reload any changes as they are made.