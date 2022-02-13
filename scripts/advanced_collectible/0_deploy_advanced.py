#!/usr/bin/python3
from brownie import AdvancedCollectible, network, config
from scripts.helpful_scripts import fund_with_link, get_publish_source, get_account


def main():
    dev = get_account()
    print(network.show_active())
    advanced_collectible = AdvancedCollectible.deploy(
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link_token"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": dev},
        publish_source=get_publish_source(),
    )
    fund_with_link(advanced_collectible.address)
    return advanced_collectible
