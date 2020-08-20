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
package io.sarl.api.naming.scheme;

import io.sarl.api.naming.scheme.NameScheme;
import io.sarl.lang.annotation.SarlElementType;
import io.sarl.lang.annotation.SarlSpecification;
import org.eclipse.xtext.xbase.lib.Pure;

/**
 * Utilities for name schemes.
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
public final class NameSchemes {
  private NameSchemes() {
  }
  
  /**
   * Parse the scheme for a named object.
   */
  @Pure
  public static NameScheme getSchemeObject(final String scheme) {
    if ((scheme != null)) {
      NameScheme[] _values = NameScheme.values();
      for (final NameScheme s : _values) {
        boolean _equalsIgnoreCase = scheme.equalsIgnoreCase(s.name());
        if (_equalsIgnoreCase) {
          return s;
        }
      }
    }
    return null;
  }
}
