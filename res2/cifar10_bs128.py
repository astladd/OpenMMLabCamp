# optimizer
optimizer = dict(type='SGD', lr=0.005, momentum=0.5, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(policy='step', step=[100, 150])
runner = dict(type='EpochBasedRunner', max_epochs=6)
