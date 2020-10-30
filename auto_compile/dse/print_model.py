filename = 'network_out.model'

with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.strip('\n')
        content = line.split(';')
        if content[1] == 'ConcatV2':
            layer_name = content[0]
            layer_type = content[1]
            input_channels = content[2].strip("][").split(', ')
            output_channel = content[3]
            input_layers = content[4:]

            print(" ===========> layer: " + layer_name)
            print("\t layer_type = " + layer_type)
            print("\t channels = " + str(input_channels))
            print("\t output_channel = " + output_channel)
            for i, il in enumerate(input_layers):
                print(f"\t input_layer {i} = " + il)
 

        else:
            tensors = (content[0].strip('][')).split(', ')
            layer_name = tensors[0].strip("'")
            input_tensor = tensors[1].strip("'")
            layer_type = content[1]
            in_channel = content[2]
            out_channel = content[3]
            expansion_factor = content[4]
            filter_ = content[5]
            stride = content[6]
            relu = content[7]
            relu6 = content[8]
            batchnorm = content[9]
            biasAdd = content[10]
            Add = content[11]
            InNumTile = content[12]
            OutNumTile = content[13]
            HeightTile = content[14]
            WidthTile = content[15]

            print(" ===========> layer: " + layer_name)
            print("\t input_tensor = " + input_tensor)
            print("\t layer_type = " + layer_type)
            print("\t in_channel = " + in_channel)
            print("\t out_channel = " + out_channel)
            print("\t expansion_factor = " + expansion_factor)
            print("\t filter = " + filter_)
            print("\t stride = " + stride)
            print("\t relu = " + relu)
            print("\t relu6 = " + relu6)
            print("\t batchnorm = " + batchnorm)
            print("\t biasAdd = " + biasAdd)
            print("\t Add = " + Add)
            print("\t InNumTile = " + InNumTile)
            print("\t OutNumTile = " + OutNumTile)
            print("\t HeightTile = " + HeightTile)
            print("\t WidthTile = " + WidthTile)
