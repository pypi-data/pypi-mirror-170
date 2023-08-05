#PySDNSim

A simulation tool that uses CloudSim Plus as backend to simulate microservices for Software Defined Network. You can clone the repository here, or use

    pip install PySDMSim

Below is an example. Make sure backend.jar is at the same directory. Download from here: https://drive.google.com/file/d/1PWtYCWDBRV02VcOD1kn_J-lLbsxyfXhT/view?usp=sharing

    from PySDNSim.Backend import Backend
    from PySDNSim.Config import Config
    from PySDNSim.Host import Host
    from PySDNSim.Job import Job
    from PySDNSim.Microservice import Microservice
    from PySDNSim.NetworkService import NetworkService
    from PySDNSim.Experiment import Experiment

    from typing import List


# simulation configuration.
    sim_config = Config(seed=1024, interval=1.0, step_size=0.01)
# host configuration.
    host = Host(
        cpus=256,
        ram=102400,
        bw=100000,
        storage=1024000,
        max_power=1600.0,
        static_power=300.0,
        replicas=1,
    )

# create microservices.
    microservices: List[Microservice] = list()
    ms_lora_gateway = Microservice(
        name="lora_gateway",
        size=128,
        cpus=2,
        ram=1024,
        bw=1000,
        replicas=1,
        max_replicas=1,
        cpu_ratio=10,
        ram_ratio=128,
        bw_ratio=100,
    )
    microservices.append(ms_lora_gateway)
    ms_mqtt_broker = Microservice(
        name="mqtt_broker",
        size=512,
        cpus=2,
        ram=1024,
        bw=1000,
        replicas=1,
        max_replicas=1,
        cpu_ratio=10,
        ram_ratio=64,
        bw_ratio=50,
    )
    microservices.append(ms_mqtt_broker)
    ms_chirpstack_gateway = Microservice(
        name="chirpstack_gateway",
        size=128,
        cpus=2,
        ram=1024,
        bw=1000,
        replicas=1,
        max_replicas=1,
        cpu_ratio=10,
        ram_ratio=64,
        bw_ratio=50,
    )
    microservices.append(ms_chirpstack_gateway)
    ms_chirpstack = Microservice(
        name="chirpstack",
        size=128,
        cpus=4,
        ram=2048,
        bw=1000,
        replicas=1,
        max_replicas=1,
        cpu_ratio=50,
        ram_ratio=128,
        bw_ratio=100,
    )
    microservices.append(ms_chirpstack)
    ms_chirpstack_rest_api = Microservice(
        name="chirpstack_rest_api",
        size=128,
        cpus=2,
        ram=1024,
        bw=1000,
        replicas=1,
        max_replicas=1,
        cpu_ratio=10,
        ram_ratio=32,
        bw_ratio=25,
    )
    microservices.append(ms_chirpstack_rest_api)
    ms_postgresql = Microservice(
        name="postgresql",
        size=2048,
        cpus=2,
        ram=1024,
        bw=1000,
        replicas=1,
        max_replicas=1,
        cpu_ratio=10,
        ram_ratio=64,
        bw_ratio=100,
    )
    microservices.append(ms_postgresql)

# create network service
    ns = NetworkService(name="chirpstack", flows=1)
    for i in range(6):
        job = Job(ms=i, length=10, file_size=10000, schedule=i)
        ns.add_job(job)
    
# create second network service
    ns2 = NetworkService(name="postgresql", flows=1)
    job = Job(ms=5, length=15, file_size=10000, schedule=2)
    ns2.add_job(job)

    experiment = Experiment(
        name="example",
        config=sim_config,
        host=host,
        microservices=microservices,
        network_services=[ns, ns2],
    )

    experiment2 = Experiment(
        name="example2",
        config=sim_config,
        host=host,
        microservices=microservices,
        network_services=[ns],
    )
    experiment2.scale_all(resource="cpu", value=1)
    experiment2.set_num_flows(3)
    backend = Backend(max_num_threads=2
    
# start the simulation/experiments

You can continue to add new experiments before call "backend.stop()"

    backend.start()
    backend.add_experiment(experiment, output_path="./results")
    backend.add_experiment(experiment2, output_path="./results")
    backend.stop()
