/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ctest4;

import Areas.ITC;
import cFramework.nodes.service.Igniter;

/**
 *
 * @author armando-cinves
 */
public class CTest4 extends Igniter {

    public CTest4() {
        addArea(ITC.class.getName());
        run();
    }
    
    
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        new CTest4();
    }
    
}
