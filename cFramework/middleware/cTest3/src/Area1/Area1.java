/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Area1;

import cFramework.communications.MessageMetadata;
import cFramework.nodes.area.Area;
import conf.Names;

/**
 *
 * @author arman
 */
public class Area1 extends Area {
    
    public Area1(){
        this.ID = Names.Area1;
        this.namer = Names.class;
        addProcess(Process1.class);
    }

    @Override
    public void init(){
        log.message("Init area 1");
        for ( int i = 0 ; i < 3; i++)
            send(Names.Process1, new MessageMetadata(i), ("M " + i).getBytes());
    }
    
    @Override
    public void receive(long nodeID, byte[] data) {
        log.message(new String(data));
    }
    
}