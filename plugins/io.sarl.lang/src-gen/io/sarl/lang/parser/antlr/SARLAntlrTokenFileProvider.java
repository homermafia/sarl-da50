/* $Id: juin 22, 2016 23:12:45$
 * File is automatically generated by the Xtext language generator. Do not change it.
 *
 */
package io.sarl.lang.parser.antlr;

import java.io.InputStream;
import org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider;

public class SARLAntlrTokenFileProvider implements IAntlrTokenFileProvider {
	
	@Override
	public InputStream getAntlrTokenFile() {
		ClassLoader classLoader = getClass().getClassLoader();
    	return classLoader.getResourceAsStream("io/sarl/lang/parser/antlr/internal/InternalSARL.tokens");
	}
}
