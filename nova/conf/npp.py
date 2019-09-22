from oslo_config import cfg

npp_group = cfg.OptGroup(
    'npp',
    title='NPP Options',
    help="""
    This Group contains options for configuring NPP schedulers in Nova
    """,
)

NPP_OPTS = [
    cfg.StrOpt(
        'simulated_host',
        help="""
        Hostname of the simulated host. 
        For all simulated servers, we need a physical host that all simulated 
        ones will map to.
        """),
    cfg.StrOpt(
        'target_cell_uuid',
        help="""
        When creating a simulated HostState, target_cell_uuid is needed
        """),
    cfg.StrOpt(
        'rabbit_username',
        help="""
        RabbitMQ username for npp schedulers
        """),
    cfg.StrOpt(
        'rabbit_password',
        help="""
        RabbitMQ password for npp schedulers
        """),
    cfg.StrOpt(
        'rabbit_host',
        help="""
        RabbitMQ host for npp schedulers
        """),
]

def register_opts(conf):
    conf.register_group(npp_group)
    conf.register_opts(NPP_OPTS, group=npp_group)

def list_opts():
    return {npp_group: NPP_OPTS}