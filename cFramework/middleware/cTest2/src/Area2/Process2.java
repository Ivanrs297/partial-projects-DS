/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Area2;

import conf.Names;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author arman
 */
public class Process2 extends cFramework.nodes.process.Process{

    public Process2(){
        this.ID = Names.Process2;
        this.namer = Names.class;
    }
    
    @Override
    public void receive(long nodeID, byte[] data) {
        log.message("Recivido en area 2, proceso muy pesado");
        try {
            Thread.sleep(5000);
        } catch (InterruptedException ex) {
            System.out.println("adsdsf");
        }
        send(Names.Area3,data);
    }
    
}
