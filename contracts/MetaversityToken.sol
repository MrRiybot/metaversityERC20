//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20{
    //Instead of WILLIAM and BILL you can use your names to make this token your own!
    constructor (address _founder, uint256 _initialSupply) ERC20("Metaversity","MTC"){
        _mint(_founder,_initialSupply);
    }
}