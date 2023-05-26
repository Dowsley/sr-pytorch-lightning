# DDBPN
Nao achei parametros.

```
  | Name           | Type       | Params | In sizes            | Out sizes
----------------------------------------------------------------------------------------
0 | sub_mean       | MeanShift  | 12     | [16, 3, 64, 64]     | [16, 3, 64, 64]
1 | initial        | Sequential | 7.9 K  | [16, 3, 64, 64]     | [16, 32, 64, 64]
2 | upmodules      | ModuleList | 679 K  | ?                   | ?
3 | downmodules    | ModuleList | 568 K  | ?                   | ?
4 | reconstruction | Sequential | 5.2 K  | [16, 192, 128, 128] | [16, 3, 128, 128]
5 | add_mean       | MeanShift  | 12     | [16, 3, 128, 128]   | [16, 3, 128, 128]
----------------------------------------------------------------------------------------
1.3 M     Trainable params
24        Non-trainable params
1.3 M     Total params
```

# EDSR
```
parser = ArgumentParser(parents=[parent], add_help=False)
parser.add_argument('--n_feats', type=int, default=64,
                    help='number of feature maps')
parser.add_argument('--n_resblocks', type=int, default=16,
                    help='number of residual blocks')
parser.add_argument('--res_scale', type=float, default=1,
                    help='residual scaling')
```
```

  | Name     | Type       | Params | In sizes          | Out sizes
--------------------------------------------------------------------------------
0 | sub_mean | MeanShift  | 12     | [16, 3, 64, 64]   | [16, 3, 64, 64]
1 | add_mean | MeanShift  | 12     | [16, 3, 128, 128] | [16, 3, 128, 128]
2 | head     | Sequential | 1.8 K  | [16, 3, 64, 64]   | [16, 64, 64, 64]
3 | body     | Sequential | 1.2 M  | [16, 64, 64, 64]  | [16, 64, 64, 64]
4 | tail     | Sequential | 149 K  | [16, 64, 64, 64]  | [16, 3, 128, 128]
--------------------------------------------------------------------------------
1.4 M     Trainable params
24        Non-trainable params
1.4 M     Total params


```

# RDN
```
parser.add_argument('--G0', type=int, default=64)
parser.add_argument('--kernel_size', type=int, default=3)
parser.add_argument('--rdn_config', type=str, default='B',
                    choices=['A', 'B'])
```
```
  | Name    | Type       | Params | In sizes           | Out sizes
--------------------------------------------------------------------------------
0 | SFENet1 | Conv2d     | 1.8 K  | [16, 3, 64, 64]    | [16, 64, 64, 64]
1 | SFENet2 | Conv2d     | 36.9 K | [16, 64, 64, 64]   | [16, 64, 64, 64]
2 | _RDBs   | ModuleList | 21.8 M | ?                  | ?
3 | GFF     | Sequential | 102 K  | [16, 1024, 64, 64] | [16, 64, 64, 64]
4 | UPNet   | Sequential | 149 K  | [16, 64, 64, 64]   | [16, 3, 128, 128]
--------------------------------------------------------------------------------
22.1 M    Trainable params
0         Non-trainable params
22.1 M    Total params
```

# RCAN
```
parser.add_argument('--n_feats', type=int, default=64,
                    help='number of feature maps')
parser.add_argument('--n_resblocks', type=int, default=16,
                    help='number of residual blocks')
parser.add_argument('--n_resgroups', type=int, default=10,
                    help='number of residual groups')
parser.add_argument('--reduction', type=int, default=16,
                    help='number of feature maps reduction')
parser.add_argument('--res_scale', type=float, default=1,
                    help='residual scaling')
```
```
  | Name     | Type       | Params | In sizes          | Out sizes
--------------------------------------------------------------------------------
0 | sub_mean | MeanShift  | 12     | [16, 3, 64, 64]   | [16, 3, 64, 64]
1 | head     | Sequential | 1.8 K  | [16, 3, 64, 64]   | [16, 64, 64, 64]
2 | body     | Sequential | 12.3 M | [16, 64, 64, 64]  | [16, 64, 64, 64]
3 | tail     | Sequential | 149 K  | [16, 64, 64, 64]  | [16, 3, 128, 128]
4 | add_mean | MeanShift  | 12     | [16, 3, 128, 128] | [16, 3, 128, 128]
--------------------------------------------------------------------------------
12.5 M    Trainable params
24        Non-trainable params
12.5 M    Total params
```
# SRCNN
Nao achei nenhum.
```
  | Name | Type       | Params | In sizes          | Out sizes
----------------------------------------------------------------------------
0 | _net | Sequential | 20.1 K | [16, 3, 128, 128] | [16, 3, 128, 128]
----------------------------------------------------------------------------
20.1 K    Trainable params
0         Non-trainable params
20.1 K    Total params
0.080     Total estimated model params size (MB)
```

# SRRESNET
```
parser.add_argument('--n_resblocks', type=int, default=16,
                    help='number of residual blocks')
parser.add_argument('--n_feats', type=int, default=64,
                    help='number of feature maps')
```
```
  | Name | Type       | Params | In sizes         | Out sizes
---------------------------------------------------------------------------
0 | head | BasicBlock | 15.6 K | [16, 3, 64, 64]  | [16, 64, 64, 64]
1 | body | Sequential | 1.2 M  | [16, 64, 64, 64] | [16, 64, 64, 64]
2 | tail | Sequential | 163 K  | [16, 64, 64, 64] | [16, 3, 128, 128]
---------------------------------------------------------------------------
1.4 M     Trainable params
0         Non-trainable params
1.4 M     Total params
```

# WDSR
```
parser.add_argument('--n_feats', type=int, default=128,
                    help='number of features to use in conv')
parser.add_argument('--n_resblocks', type=int, default=16,
                    help='number of residual blocks')
parser.add_argument('--res_scale', type=float, default=1,
                    help='residual scaling')
parser.add_argument('--type', type=str, default='B',
                    choices=['A', 'B'])
```
```
  | Name | Type       | Params | In sizes          | Out sizes
----------------------------------------------------------------------------
0 | head | Sequential | 3.7 K  | [16, 3, 64, 64]   | [16, 128, 64, 64]
1 | body | Sequential | 4.7 M  | [16, 128, 64, 64] | [16, 128, 64, 64]
2 | tail | Sequential | 13.8 K | [16, 128, 64, 64] | [16, 3, 128, 128]
3 | skip | Sequential | 924    | [16, 3, 64, 64]   | [16, 3, 128, 128]
----------------------------------------------------------------------------
4.8 M     Trainable params
0         Non-trainable params
4.8 M     Total params
```