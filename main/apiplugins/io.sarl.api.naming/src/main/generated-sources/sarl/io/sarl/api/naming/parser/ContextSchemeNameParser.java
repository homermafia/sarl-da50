/**
 * $Id$
 * 
 * SARL is an general-purpose agent programming language.
 * More details on http://www.sarl.io
 * 
 * Copyright (C) 2014-2020 the original authors or authors.
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package io.sarl.api.naming.parser;

import io.sarl.api.naming.name.ContextName;
import io.sarl.api.naming.parser.AbstractSchemeNameParser;
import io.sarl.api.naming.scheme.NameScheme;
import io.sarl.lang.annotation.DefaultValue;
import io.sarl.lang.annotation.DefaultValueSource;
import io.sarl.lang.annotation.DefaultValueUse;
import io.sarl.lang.annotation.SarlElementType;
import io.sarl.lang.annotation.SarlSourceCode;
import io.sarl.lang.annotation.SarlSpecification;
import io.sarl.lang.annotation.SyntheticMember;
import java.net.URI;
import java.util.StringTokenizer;
import java.util.UUID;
import org.eclipse.xtext.xbase.lib.Pure;

/**
 * Parser of context names that is accepting URI-based syntax.
 * 
 * <p>The different types of names are: <ul>
 * <li>{@code "context:[/]{0-2}contextId[#fragmentName]"}</li>
 * </ul>
 * 
 * @author $Author: sgalland$
 * @version $FullVersion$
 * @mavengroupid $GroupId$
 * @mavenartifactid $ArtifactId$
 * @since 0.12
 */
@SarlSpecification("0.12")
@SarlElementType(10)
@SuppressWarnings("all")
public class ContextSchemeNameParser extends AbstractSchemeNameParser<ContextName> {
  /**
   * Constructor.
   * 
   * @param scheme the name scheme that is supported by this parser. By default it is {@link NameScheme.CONTEXT}.
   */
  @DefaultValueSource
  public ContextSchemeNameParser(@DefaultValue("io.sarl.api.naming.parser.ContextSchemeNameParser#NEW_0") final NameScheme scheme) {
    super(scheme);
  }
  
  /**
   * Default value for the parameter scheme
   */
  @SyntheticMember
  @SarlSourceCode("NameScheme::CONTEXT")
  private static final NameScheme $DEFAULT_VALUE$NEW_0 = NameScheme.CONTEXT;
  
  @Pure
  @Override
  public URI refactor(final URI name) {
    return this.refactor(name, 1, 1);
  }
  
  @Pure
  @Override
  public ContextName decode(final URI name) {
    String _path = name.getPath();
    final StringTokenizer tokenizer = new StringTokenizer(_path, "/");
    boolean _hasMoreTokens = tokenizer.hasMoreTokens();
    if (_hasMoreTokens) {
      final String token = tokenizer.nextToken();
      UUID _fromString = UUID.fromString(token);
      return new ContextName(name, _fromString);
    }
    return null;
  }
  
  /**
   * Constructor.
   * 
   * @optionalparam scheme the name scheme that is supported by this parser. By default it is {@link NameScheme.CONTEXT}.
   */
  @DefaultValueUse("io.sarl.api.naming.scheme.NameScheme")
  @SyntheticMember
  public ContextSchemeNameParser() {
    this($DEFAULT_VALUE$NEW_0);
  }
}
