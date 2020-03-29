/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Sensor2;

import cFramework.nodes.area.Area;
import conf.Names;

/**
 *
 * @author arman
 */
public class Sensor2 extends Area {
    
    public Sensor2(){
        this.ID = Names.Sensor2;
        this.namer = Names.class;
    }

    @Override
    public void init(){
        for ( int i = 0; i < 5 ; i++ ) 
            try {
                send(Names.Server, ("S2-" + 1).getBytes());
                Thread.sleep(5000);
            }catch(Exception e ) { 
                
            }
        
    }
    
    @Override
    public void receive(long nodeID, byte[] data) {
        
    }
    
}