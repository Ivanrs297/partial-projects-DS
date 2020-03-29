/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Area1;

import conf.Names;

/**
 *
 * @author arman
 */
public class Process1 extends cFramework.nodes.process.Process {
    
    public Process1 () {
        this.ID = Names.Process1;
        this.namer = Names.class;
    }

    @Override
    public void receive(long nodeID, byte[] data) {
        log.message("Recibido en proceso 1");
        send(Names.Area2,data);        
        send(Names.Area3,data);

    }
    
}
