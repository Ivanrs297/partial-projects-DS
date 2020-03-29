/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Sensor1;

import cFramework.nodes.area.Area;
import conf.Names;

/**
 *
 * @author arman
 */
public class Sensor1 extends Area {
    
    public Sensor1(){
        this.ID = Names.Sensor1;
        this.namer = Names.class;
    }

    @Override
    public void init(){
        for ( int i = 0; i < 10 ; i++ ) 
            try {
                send(Names.Server, ("S1-" + 1).getBytes());
                Thread.sleep(5000);
            }catch(Exception e ) { 
                
            }
        
    }
    
    @Override
    public void receive(long nodeID, byte[] data) {
        
    }
    
}