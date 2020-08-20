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
package io.sarl.api.naming.namespace;

import io.sarl.api.naming.name.SarlName;
import io.sarl.api.naming.scheme.NameScheme;
import io.sarl.lang.annotation.SarlElementType;
import io.sarl.lang.annotation.SarlSpecification;
import org.eclipse.xtext.xbase.lib.Pure;

/**
 * A tool that is able to find a specific type of object from a name into the SRE.
 * Each type of element (agent, behavior, etc.) has a specific and dediciated implementation
 * of finder. Of course, the finder's implementation depends strongly on the SRE implementation
 * itself.
 * 
 * @param <N> the type of name that is supported by this finder.
 * @param <O> the type of object that is searching for.
 * @author $Author: sgalland$
 * @version $FullVersion$
 * @mavengroupid $GroupId$
 * @mavenartifactid $ArtifactId$
 * @since 0.12
 */
@SarlSpecification("0.12")
@SarlElementType(11)
@SuppressWarnings("all")
public interface INamespaceFinder<N extends SarlName, O extends Object> {
  /**
   * Replies the name scheme supported by this finder.
   */
  @Pure
  NameScheme getScheme();
  
  /**
   * Find and replies the object with the given name.
   * 
   * @param name the name of the object to search for.
   * @return the object, or {@code null} if the object is not found.
   */
  @Pure
  O find(final N name);
}
