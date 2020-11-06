network_inst = "../inst_gen/network.insts"


def to_binary_32bit(a):
    # little endian
    b = f'{a:032b}'
    b = b[::-1]
    return b

def split(orig, dest):
    result = list()
    bit_str = to_binary_32bit(orig)
    for i in range(0, len(bit_str), dest):
        string = ''
        for j in range(dest):
            string += bit_str[i + j]
        element = int(string, base=2)
        result.append(element)
    return result

with open(network_inst, "r") as f:
    lines = f.readlines()

layer_idx = 0
for i in range(0, len(lines), 6):
    # fetch the instructions
    inst0 = lines[i]
    inst1 = lines[i+1]
    inst2 = lines[i+2]
    inst3 = lines[i+3]
    inst4 = lines[i+4]
    # split instructions
    inst0 = [int(x) for x in inst0.split()]
    inst1 = [int(x) for x in inst1.split()]
    inst2 = [int(x) for x in inst2.split()]
    inst3 = [int(x) for x in inst3.split()]
    inst4 = [int(x) for x in inst4.split()]

    print(f"=====> layer number: {layer_idx}")
    
    # decode inst0
    print(f'\t inst0: ')
    print(f'\t in_num_hw   = {inst0[0]}')
    print(f'\t out_num_hw  = {inst0[1]}') 
    print(f'\t in_h_hw     = {inst0[2]}') 
    print(f'\t in_w_hw     = {inst0[3]}') 
    print(f'\t out_w_hw    = {inst0[4]}')
    print(f'\t out_h_hw    = {inst0[5]}')
    # decode inst1
    print(f'\n inst1:')
    print(f'\t in_num   = {inst1[0]}')
    print(f'\t out_num  = {inst1[1]}') 
    print(f'\t in_h     = {inst1[2]}') 
    print(f'\t in_w     = {inst1[3]}') 
    print(f'\t out_w    = {inst1[4]}')
    print(f'\t out_h    = {inst1[5]}')
    # decode inst2
    print(f'\n inst2:')
    print(f'\t cin_offset      = {inst2[0]}')
    print(f'\t weight_offset   = {inst2[1]}') 
    print(f'\t bias_offset     = {inst2[2]}') 
    print(f'\t cout_offset     = {inst2[3]}')
    filter_s = split(inst2[4], 16)
    print(f'\t filter_s1 = {filter_s[0]}')
    print(f'\t filter_s2 = {filter_s[1]}')
    print(f'\t stride          = {inst2[5]}')
    # decode inst3
    # notice that in the hardware decoding, int_num_t and out_num_t are squeezed together
    # each is 16-bit
    print(f'\n inst3: ')
    layer_en = split(inst3[0], 1)
    print(f'\t conv_1st_en = {layer_en[0]}    depth_conv_en = {layer_en[1]}    conv_en = {layer_en[2]}')
    print(f'\t relu_en = {layer_en[3]}        relu6_en = {layer_en[4]}         pool_en = {layer_en[5]}')
    print(f'\t up_sample_en = {layer_en[6]}   bias_en = {layer_en[7]}          inter_load_en = {layer_en[8]}')
    print(f'\t inter_write_en = {layer_en[9]} batch_norm_en_conv = {layer_en[10]} load_prev_cin = {layer_en[11]}')
    print(f'\t batch_norm_en_depth = {layer_en[12]}')
    print(f'\t prev_cin_offset     = {inst3[1]}')
    print(f'\t in_num_t = {inst3[2]}')
    print(f'\t out_num_t = {inst4[3]}')
    print(f'\t in_h_t = {inst3[4]}')
    print(f'\t in_w_t = {inst3[5]}')
    print(f'\t next_layer_batch = {inst3[6]}')
    # decode inst4
    print(f'\n inst4: (for systolic array)')
    print(f'\t task_num1        = {inst4[0]}')
    print(f'\t task_num2        = {inst4[1]}') 
    print(f'\t local_accum_num  = {inst4[2]}') 
    print(f'\t local_reg_num    = {inst4[3]}') 
    print(f'\t row_il_factor    = {inst4[4]}')
    print(f'\t col_il_factor    = {inst4[5]} \n') 