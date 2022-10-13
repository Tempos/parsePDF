# Parse PDF

Parse AWS pdf file for endpoints, using tabula library.

### Instalation:
```pip install -r requirements.txt```


### Example JSON, generated from a PDF table:

| Region Name            | Region    | Endpoint                        | Protocol |     |
|------------------------|-----------|---------------------------------|----------|-----|
| US East (Ohio)         | us-east-2 | amplify.us-east-2.amazonaws.com | HTTPS    |     |
| US East (N. Virginia)  | us-east-1 | amplify.us-east-1.amazonaws.com | HTTPS    |     |

```json
[{
    "extraction_method": "lattice", "top": 79.27209, "left": 120.00431, "width": 437.9960632324219,
    "height": 50.08702850341797, "right": 558.00037, "bottom": 129.35912,
    "data": [
        [{"top": 288.1747, "left": 120.00431, "width": 54.748374938964844, "height": 30.44317626953125,
          "text": "Region\rName"},
         {"top": 288.1747, "left": 174.75269, "width": 54.75, "height": 30.44317626953125, "text": "Region"},
         {"top": 288.1747, "left": 229.50269, "width": 219.0, "height": 30.44317626953125, "text": "Endpoint"},
         {"top": 288.1747, "left": 448.5027, "width": 54.75, "height": 30.44317626953125, "text": "Protocol"},
         {"top": 288.1747, "left": 503.2527, "width": 54.7476806640625, "height": 30.44317626953125, "text": ""}],
        [{"top": 318.6179, "left": 120.00431, "width": 54.748374938964844, "height": 30.639617919921875, "text": "US East\r(Ohio)"},
         {"top": 318.6179, "left": 174.75269, "width": 54.75, "height": 30.639617919921875, "text": "us-east-2"},
         {"top": 318.6179, "left": 229.50269, "width": 219.0, "height": 30.639617919921875, "text": "amplify.us-east-2.amazonaws.com"},
         {"top": 318.6179, "left": 448.5027, "width": 54.75, "height": 30.639617919921875, "text": "HTTPS"},
         {"top": 318.6179, "left": 503.2527, "width": 54.7476806640625, "height": 30.639617919921875, "text": ""}],
        [{"top": 349.2575, "left": 120.00431, "width": 54.748374938964844, "height": 30.580108642578125, "text": "US East (N.\rVirginia)"},
         {"top": 349.2575, "left": 174.75269, "width": 54.75, "height": 30.580108642578125, "text": "us-east-1"},
         {"top": 349.2575, "left": 229.50269, "width": 219.0, "height": 30.580108642578125, "text": "amplify.us-east-1.amazonaws.com"},
         {"top": 349.2575, "left": 448.5027, "width": 54.75, "height": 30.580108642578125, "text": "HTTPS"},
         {"top": 349.2575, "left": 503.2527, "width": 54.7476806640625, "height": 30.580108642578125, "text": ""}]
    ]
}]

```
