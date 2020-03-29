/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Area1;

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
        for ( int i = 0; i < 1 ; i++ ) 
            try {
                send(Names.Process1, ("M " + 1).getBytes());
                Thread.sleep(5000);
            }catch(Exception e ) { 
                
            }
        
    }
    
    @Override
    public void receive(long nodeID, byte[] data) {
        
    }
    
}