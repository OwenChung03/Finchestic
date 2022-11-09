// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IERC20Basic {
   function balanceOf(address who) {public returns (uint)};
   function transfer(address to, uint value) public returns (bool ok);
   event Transfer(address indexed from, address indexed to, uint value);
}
