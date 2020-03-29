/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Area3;

import Area1.*;
import cFramework.nodes.area.Area;
import conf.Names;

/**
 *
 * @author arman
 */
public class Area3 extends Area {
    
    public Area3(){
        this.ID = Names.Area3;
        this.namer = Names.class;
        addProcess(Process3.class);
    }
    
    @Override
    public void receive(long nodeID, byte[] data) {
        log.message("Recivido area 3");
        send(Names.Process3, data);
    }
    
}