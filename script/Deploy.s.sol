// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script} from "forge-std/Script.sol";
import {console2} from "forge-std/console2.sol";

import { SelfGateRegistry } from "src/SelfGateRegistry.sol";

contract Deploy is Script {
    function run() external returns (SelfGateRegistry deployed) {
        address admin = vm.envAddress("ADMIN_WALLET_ADDRESS");
        address operator = vm.envAddress("OPERATOR_WALLET_ADDRESS");

        vm.startBroadcast();
        deployed = new SelfGateRegistry(admin, operator);
        vm.stopBroadcast();

        console2.log("Deployed SelfGateRegistry at", address(deployed));
    }
}
