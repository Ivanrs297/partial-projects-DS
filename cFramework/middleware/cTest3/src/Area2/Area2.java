/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Area2;

import cFramework.nodes.area.Area;
import cFramework.nodes.process.ProcessConfiguration;
import conf.Names;

/**
 *
 * @author arman
 */
public class Area2 extends Area {

    public Area2(){
        this.ID = Names.Area2;
        this.namer = Names.class;
        addProcess(Process2.class, ProcessConfiguration.TYPE_PARALLEL);
    }
    
    
    @Override
    public void receive(long nodeID, byte[] data) {
        log.message("Recivido area 2");
        send(Names.Process2, data);
    }
    
}
