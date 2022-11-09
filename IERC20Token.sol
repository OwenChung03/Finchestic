
pragma solidity ^0.8.0;
import "./IERC20Basic.sol";

/*
 * ERC20 interface
 * see https://github.com/ethereum/EIPs/issues/20
 */
contract IERC20Token is IERC20Basic {
  function totalSupply() public returns (uint256);
  function allowance(address owner, address spender) returns (uint);
  function transferFrom(address from, address to, uint value) returns (bool ok);
  function approve(address spender, uint value) returns (bool ok);
  event Approval(address indexed owner, address indexed spender, uint value);
}
