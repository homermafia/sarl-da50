/*
 * $Id$
 *
 * SARL is an general-purpose agent programming language.
 * More details on http://www.sarl.io
 *
 * Copyright (C) 2014-2021 the original authors or authors.
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

package io.sarl.lang.util;

import java.util.Collection;
import java.util.concurrent.CopyOnWriteArrayList;

/** Represent a list of objects with is thread-safe.
 *
 * @param <T> the type of the objects in the list.
 * @author $Author: sgalland$
 * @version $FullVersion$
 * @mavengroupid $GroupId$
 * @mavenartifactid $ArtifactId$
 * @since 0.12
 */
public class ConcurrentListCopyOnWriteList<T> extends CopyOnWriteArrayList<T> implements ConcurrentList<T> {

	private static final long serialVersionUID = 1160714015698422513L;

	/**
     * Creates an empty list.
     */
	public ConcurrentListCopyOnWriteList() {
        super();
    }

    /**
     * Creates a list containing the elements of the specified
     * collection, in the order they are returned by the collection's
     * iterator.
     *
     * @param source the collection of initially held elements
     * @throws NullPointerException if the specified collection is null
     */
    public ConcurrentListCopyOnWriteList(Collection<? extends T> source) {
        super(source);
    }

    /**
     * Creates a list holding a copy of the given array.
     *
     * @param toCopyIn the array (a copy of this array is used as the
     *        internal array)
     * @throws NullPointerException if the specified array is null
     */
    public ConcurrentListCopyOnWriteList(T[] toCopyIn) {
        super(toCopyIn);
    }

}